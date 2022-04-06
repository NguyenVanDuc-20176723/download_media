import requests
import time
import re
import os
session = requests.session()

def download_media(url):
    file_name = re.findall(r"[^/]+\.mp4", url)
    if len(file_name) == 1:
        file_name = file_name[0]
        print(f"Downloading file \"{file_name}\"")
        start = time.time()
        res = session.get(url, stream=True)
        total_size = int(res.headers._store['content-length'][1])
        size = 0
        # i = 1
        while True:
            try:
                with open(file_name, "ab") as f:
                    for truck in res.iter_content(chunk_size=2**20):
                        if truck:
                            f.write(truck)
                            size += 2**20
                            print(f"size: {size} / {total_size} Byte")
                            # if size > 100000000*i:
                            #     i += 1
                            #     break
                    f.close()
            except Exception as e:
                print(e)
                f.close()
            size = os.path.getsize(file_name)
            print(f"Size of file {file_name} is {size} Byte")
            if size >= total_size:
                print(f"Download complated {time.time() - start}s")
                break
            res = session.get(url, headers={"range": f"bytes={size}-"}, stream=True)





if __name__ == '__main__':
    video_url = "https://video.fhan2-3.fna.fbcdn.net/v/t42.1790-2/10000000_374824821161568_1563667437205500971_n.mp4?_nc_cat=107&vs=4ea562f7981c0f76&_nc_vs=HBksFQAYJEdJQ1dtQUJnZmxHMDVsUUJBQ3UwZXQwLVE3TVZidjRHQUFBRhUAAsgBABUAGCRHSUNXbUFCTW02TWNwNmNCQUpaSkxLN2tzV2h1YnY0R0FBQUYVAgLIAQAoRC1pICclcycgLWZiX3VzZV90ZmR0X3N0YXJ0dGltZSAxIC1pICclcycgLWMgY29weSAtbW92ZmxhZ3MgZmFzdHN0YXJ0KwaIEnByb2dyZXNzaXZlX3JlY2lwZQExDXN1YnNhbXBsZV9mcHMAEHZtYWZfZW5hYmxlX25zdWIAIG1lYXN1cmVfb3JpZ2luYWxfcmVzb2x1dGlvbl9zc2ltAChjb21wdXRlX3NzaW1fb25seV9hdF9vcmlnaW5hbF9yZXNvbHV0aW9uABFkaXNhYmxlX3Bvc3RfcHZxcwAVACUAHAAAJpLqkI31gu4SFZBOKAJDMxgDYXYxHBdAyG9hR64UexgZZGFzaF9saXZlX21kX2ZyYWdfMl92aWRlbxIAGBh2aWRlb3MudnRzLmNhbGxiYWNrLnByb2QZHBUAFfK2BAAoElZJREVPX1ZJRVdfUkVRVUVTVBsOiBVvZW1fdGFyZ2V0X2VuY29kZV90YWcGb2VwX3NkE29lbV9yZXF1ZXN0X3RpbWVfbXMBMAxvZW1fY2ZnX3J1bGUKd2FzbGl2ZV9zZBNvZW1fcm9pX3JlYWNoX2NvdW50BDY1NjMRb2VtX2lzX2V4cGVyaW1lbnQADG9lbV9yb2lfbm90ZQtwcm9ncmVzc2l2ZRFvZW1fcm9pX3VzZXJfdGllcgAeb2VtX3JvaV9wcmVkaWN0ZWRfd2F0Y2hfdGltZV9zATAWb2VtX3JvaV9yZWNpcGVfYmVuZWZpdAUwLjAwMCVvZW1fcm9pX3N0YXRpY19iZW5lZml0X2Nvc3RfZXZhbHVhdG9yC3Byb2dyZXNzaXZlDG9lbV92aWRlb19pZA81MTUxNjE1OTY2Nzg5NzQSb2VtX3ZpZGVvX2Fzc2V0X2lkDzcwMzc0NDc0NzY0ODU0MRVvZW1fdmlkZW9fcmVzb3VyY2VfaWQQNTMwODQ5MjIxNTg4NDQyNRxvZW1fc291cmNlX3ZpZGVvX2VuY29kaW5nX2lkDzUwMTc2NTA5NDk2MjY2MyUEHBwcFfDmFxsBVQACGwFVAAIcFQIAAAAWgLq3AwAlxAEbB4gBcwQ4MDUzAmNkCjIwMjItMDMtMjkDcmNiBDY1MDADYXBwHENvbnRlbnQgVGFiIG9mIGEgUGFnZSBvbiB3d3cCY3QJQlJPQURDQVNUE29yaWdpbmFsX2R1cmF0aW9uX3MJMTI1MTAuODQ5AnRzFHByb2dyZXNzaXZlX29yZGVyaW5nAA%3D%3D&ccb=1-5&_nc_sid=a1bfcc&_nc_ohc=FYLR0rNNgA8AX8ebTe_&_nc_ht=video.fhan2-3.fna&oh=00_AT_kxNzaYj-wlB7gtfoP_8zn6zDoR62QIgMaaUMAcKwAWg&oe=624DD1BD&_nc_rid=576477273438486"
    download_media(video_url)

