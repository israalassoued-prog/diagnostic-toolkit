
import socket
import time


def check_dns(hostname: str) -> dict:
    """Check whether a hostname can be resolved."""
    try:
        start = time.perf_counter()
        ip_address = socket.gethostbyname(hostname)
        elapsed_ms = (time.perf_counter() - start) * 1000

        return {
            "check": "DNS Resolution",
            "target": hostname,
            "status": "PASS",
            "details": f"Resolved to {ip_address}",
            "response_ms": round(elapsed_ms, 2),
        }

    except socket.gaierror as error:
        return {
            "check": "DNS Resolution",
            "target": hostname,
            "status": "FAIL",
            "details": f"Hostname resolution failed: {error}",
            "response_ms": None,
        }


def check_tcp(hostname: str, port: int, timeout: float = 3.0) -> dict:
    """Test whether a TCP connection can be established."""
    start = time.perf_counter()

    try:
        with socket.create_connection(
            (hostname, port), timeout=timeout
        ):
            elapsed_ms = (time.perf_counter() - start) * 1000

        return {
            "check": "TCP Connectivity",
            "target": f"{hostname}:{port}",
            "status": "PASS",
            "details": "TCP connection established",
            "response_ms": round(elapsed_ms, 2),
        }

    except socket.timeout:
        return {
            "check": "TCP Connectivity",
            "target": f"{hostname}:{port}",
            "status": "FAIL",
            "details": "Connection timed out",
            "response_ms": None,
        }

    except OSError as error:
        return {
            "check": "TCP Connectivity",
            "target": f"{hostname}:{port}",
            "status": "FAIL",
            "details": str(error),
            "response_ms": None,
        }
