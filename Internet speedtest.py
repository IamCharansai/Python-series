import speedtest

def test_internet_speed():
    print("Testing your internet speed. Please wait...\n")
    st = speedtest.Speedtest()

    download_speed = st.download() / 1_000_000  # in Mbps
    upload_speed = st.upload() / 1_000_000      # in Mbps
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

# Run the test
test_internet_speed()
