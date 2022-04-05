import progressbar
import urllib.request

url_video = "https://video-hkg4-2.xx.fbcdn.net/v/t39.25447-2/277355253_497688865357741_313726009800969579_n.mp4?_nc_cat=111&vs=56007231b771a35d&_nc_vs=HBksFQAYJEdQVWFpQkN0UHdjNHBjUUJBR3ZOLU1va2xGb0VibWRqQUFBRhUAAsgBABUAGCRHQUpVZ3hDSGRSaFFnNHNGQU9nWkNqZGo0dlJMYnJGcUFBQUYVAgLIAQBLBogScHJvZ3Jlc3NpdmVfcmVjaXBlATENc3Vic2FtcGxlX2ZwcwAQdm1hZl9lbmFibGVfbnN1YgAgbWVhc3VyZV9vcmlnaW5hbF9yZXNvbHV0aW9uX3NzaW0AKGNvbXB1dGVfc3NpbV9vbmx5X2F0X29yaWdpbmFsX3Jlc29sdXRpb24AEWRpc2FibGVfcG9zdF9wdnFzABUAJQAcAAAmzN%2Bi%2BZfprAEVkE4oAkMzGAt2dHNfcHJldmlldxwXQDyAAAAAAAAYIGRhc2hfdjRfNXNlY2dvcF9ocTJfZnJhZ18yX3ZpZGVvEgAYGHZpZGVvcy52dHMuY2FsbGJhY2sucHJvZDgSVklERU9fVklFV19SRVFVRVNUGw6IFW9lbV90YXJnZXRfZW5jb2RlX3RhZwZvZXBfaGQTb2VtX3JlcXVlc3RfdGltZV9tcwEwDG9lbV9jZmdfcnVsZQd1bm11dGVkE29lbV9yb2lfcmVhY2hfY291bnQENjU2MxFvZW1faXNfZXhwZXJpbWVudAAMb2VtX3JvaV9ub3RlC3Byb2dyZXNzaXZlEW9lbV9yb2lfdXNlcl90aWVyAB5vZW1fcm9pX3ByZWRpY3RlZF93YXRjaF90aW1lX3MBMBZvZW1fcm9pX3JlY2lwZV9iZW5lZml0BTAuMDAwJW9lbV9yb2lfc3RhdGljX2JlbmVmaXRfY29zdF9ldmFsdWF0b3ILcHJvZ3Jlc3NpdmUMb2VtX3ZpZGVvX2lkEDExNDgxMTUxNTIzOTcwNDMSb2VtX3ZpZGVvX2Fzc2V0X2lkDzY2NjIzODA3NzgyMjg4NBVvZW1fdmlkZW9fcmVzb3VyY2VfaWQPMzgwMDM5MTAwMzg5MzUwHG9lbV9zb3VyY2VfdmlkZW9fZW5jb2RpbmdfaWQQMTE0MDkwMTU4MDAwMzE5NyUCHBwcFfDmFxsBVQACGwFVAAIcFQIAAAAWgLq3AwAlxAEbB4gBcwM3NzMCY2QKMjAyMi0wMy0yNQNyY2IENjUwMANhcHAURmFjZWJvb2sgZm9yIEFuZHJvaWQCY3QZQ09OVEFJTkVEX1BPU1RfQVRUQUNITUVOVBNvcmlnaW5hbF9kdXJhdGlvbl9zBjI4LjYwMgJ0cxVwcm9ncmVzc2l2ZV9lbmNvZGluZ3MA&ccb=1-5&_nc_sid=a1bfcc&_nc_ohc=aw_-b4-0W4cAX-pRIRB&_nc_ht=video-hkg4-2.xx&oh=00_AT8BCOqh6ns_JPKW32lHgPC6yewO2s3UzpChTjr_41D1aA&oe=6251FA3A&_nc_rid=718933884927240"


# pbar = None
#
#
# def show_progress(block_num, block_size, total_size):
#     global pbar
#     if pbar is None:
#         pbar = progressbar.ProgressBar(maxval=total_size)
#         pbar.start()
#
#     downloaded = block_num * block_size
#     if downloaded < total_size:
#         pbar.update(downloaded)
#     else:
#         pbar.finish()
#         pbar = None

class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar = progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()


urllib.request.urlretrieve(url_video, 'video_name.mp4', MyProgressBar())
