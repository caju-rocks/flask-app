import ssl
import socket
import time
import requests
import hashlib

DOMAIN = "debug.qa.liverpool.bluecharm.cloud"
LOGFILE = "monitor.log"

last_fingerprint = None
current_fail_start = None
total_downtime = 0

print(f"Monitoring {DOMAIN} — logged in {LOGFILE}")
print("---------------------------------------")

def get_certificate_fingerprint(cert_bin):
    sha256 = hashlib.sha256(cert_bin).hexdigest()
    return sha256.upper()

def check_cert(domain):
    ctx = ssl.create_default_context()
    with socket.create_connection((domain, 443), timeout=5) as sock:
        with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
            cert_bin = ssock.getpeercert(binary_form=True)
            return cert_bin


def check_https(domain):
    response = requests.get(f"https://{domain}", timeout=5)
    return True, response

while True:
    ts = time.strftime("%Y-%m-%d %H:%M:%S")

    cert_ok = False
    https_ok = False

    try:
        cert = check_cert(DOMAIN)
        fingerprint = get_certificate_fingerprint(cert)
        cert_ok = True
    except Exception as e:
        fingerprint = "NONE"

    if fingerprint != "NONE" and fingerprint != last_fingerprint:
        if last_fingerprint is not None:
            print(f"[{ts}] Certificate has changed -> new fingerprint: {fingerprint}")
            with open(LOGFILE, "a") as f:
                f.write(f"[{ts}] Certificate has changed -> {fingerprint}\n")
        last_fingerprint = fingerprint

    try:
        _, response = check_https(DOMAIN)
        response_custom_header = response.json()["response_headers"]["X-Bluecharm-LB"]
        https_ok = True
    except:
        pass

    if cert_ok and https_ok:
        print(
            f"[{ts}] OK - Certificate is valid, https works, the request hit {response_custom_header}"
        )

        if current_fail_start:
            fail_duration = int(time.time() - current_fail_start)
            total_downtime += fail_duration
            print(f"[{ts}] Enf of fail – fail duration: {fail_duration}s")
            with open(LOGFILE, "a") as f:
                f.write(f"[{ts}] End of fail – {fail_duration}s\n")
            current_fail_start = None

    else:
        print(f"[{ts}] FAIL - certificate is invalid or HTTPS is broken")

        if not current_fail_start:
            current_fail_start = time.time()
            with open(LOGFILE, "a") as f:
                f.write(f"[{ts}] Fail begining\n")

    with open(LOGFILE, "a") as f:
        f.write(f"[{ts}] cert_ok={cert_ok} https_ok={https_ok} fp={fingerprint}\n")

    time.sleep(1)
