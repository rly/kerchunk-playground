import h5py

H5_STR = h5py.string_dtype("utf-8")
H5_BYTES = h5py.string_dtype("ascii")

with h5py.File("test_str.h5", "w") as f:
    f.create_dataset("data", data="test", shape=None, dtype=H5_STR)

with h5py.File("test_multi_str.h5", "w") as f:
    f.create_dataset("data", data=["test", "more test"], dtype=H5_STR)

with h5py.File("test_bytes.h5", "w") as f:
    f.create_dataset("data", data=b"test", shape=None, dtype=H5_BYTES)

with h5py.File("test_int.h5", "w") as f:
    f.create_dataset("data", data=1, shape=None, dtype=int)
