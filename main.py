import json
from datetime import datetime
from pathlib import Path
from network_diagnostics import check_dns, check_tcp
def get_recommendation(result: dict) -> str:
    if result["status"] == "PASS":
        if result["check"] == "DNS Resolution":
            return (
                "DNS resolution succeeded. If the issue persists, "
                "continue with connectivity or application-level tests."
            )

        return (
            "TCP connection succeeded. If the application still fails, "
            "investigate the service at the application level."
        )

    if result["check"] == "DNS Resolution":
        return (
            "Verify the hostname spelling and investigate DNS, "
            "network, or VPN configuration."
        )

    return (
        "Verify the hostname and port, check whether the service is "
        "available, and investigate firewall or network rules."
    )


def save_report(results: list[dict]) -> Path:
    reports_dir = Path(__file__).parent / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    report_path = reports_dir / f"network_report_{timestamp}.json"

    with report_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    return report_path


def main():
    hostname = input("Enter a hostname (e.g. example.com): ").strip()

    if not hostname:
        print("Error: hostname cannot be empty.")
        return

    results = [check_dns(hostname)]

    try:
        port = int(input("Enter a TCP port (e.g. 443): "))

        if not 1 <= port <= 65535:
            print("Error: port must be between 1 and 65535.")
            return

    except ValueError:
        print("Error: enter a valid integer for the port.")
        return

    results.append(check_tcp(hostname, port))

    print("\n=== NETWORK DIAGNOSTIC REPORT ===")

    for result in results:
        result["recommendation"] = get_recommendation(result)
        print(f"\nCheck: {result['check']}")
        print(f"Target: {result['target']}")
        print(f"Status: {result['status']}")
        print(f"Details: {result['details']}")
        print(f"Response time: {result['response_ms']} ms")
        print(f"Next step: {result['recommendation']}")

    report_path = save_report(results)
    print(f"\nReport saved to: {report_path}")

if __name__ == "__main__":
    main()
