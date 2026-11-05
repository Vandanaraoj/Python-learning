print("\n========== TASK 3 ==========")

ports = [80, 443, 1050, 21, 1500]

print("Original Ports:", ports)
print("Global Blacklist: range(1000, 2000)")

filtered_ports = filter(lambda port: port not in range(1000, 2000), ports)

print("Filtered Ports:", filtered_ports)


# Local variable with the same name

def filter_ports_local(ports):
    """
    Demonstrate Local variable shadowing Global variable.

    LEGB:
    BLACKLIST_RANGE is found in Local scope first.
    Therefore, the Local range(0, 500) is used.
    """

    BLACKLIST_RANGE = range(0, 500)

    filtered_ports = list(
        filter(
            lambda port: port not in BLACKLIST_RANGE,
            ports
        )
    )

    return filtered_ports


print("\n--- LEGB Example ---")

local_result = filter_ports_local(ports)

print("Local Blacklist: range(0, 500)")
print("Result using Local Blacklist:", local_result)