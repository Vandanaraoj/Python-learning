def analyze_traffic(source_name, *ips, **metadata):
    """
    Analyze multiple IP addresses and security metadata.

    LEGB:
    source_name, ips, and metadata are Local variables.
    """

    print("Source:", source_name)
    print("IP Addresses:", ips)
    print("Number of IPs:", len(ips))
    print("Security Tags:", list(metadata.keys()))

    result = (
        f"Source: {source_name} | "
        f"Analyzed {len(ips)} IPs | "
        f"Security Tags: {', '.join(metadata.keys())}"
    )

    return result


print("\n========== TASK 1 ==========")

result = analyze_traffic(
    "Mainframe_A",
    "192.168.1.1",
    "10.0.0.5",
    "172.16.0.1",
    threat_level="High",
    protocol="SSH"
)

print(result)