import speedtest

def run():
    print("Testing speed, please wait...")
    st = speedtest.Speedtest()
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    ping = st.results.ping
    print(f"Download: {download:.2f} Mbps\nUpload: {upload:.2f} Mbps\nPing: {ping} ms")