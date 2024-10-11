from pathlib import Path

# print(Path(r'C:\Program Files\Microsoft'))
# print(Path('/usr/local/bin'))
# path = Path('ecommerce/__init__.py')
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)  # __init__.py
# print(path.stem)  # __init__
# print(path.suffix)  # .py
# print(path.parent)  # ecommerce
# path = path.with_name('file.txt')  # ecommerce/file.txt
# print(path)
# # /media/hp/b88f4163-a61d-4759-a011-7a3803b45bd0/Courses/Courses/Learning/LearningPython/ecommerce/file.txt
# print(path.absolute())

path = Path('ecommerce')
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename('ecommerce2')

# for p in path.iterdir():  # <generator object Path.iterdir at 0x70a2248879f0>
#     print(p)  # ecommerce/__init__.py -> ecommerce/shopping
# with comprehension
# paths = [p for p in path.iterdir()]
# [PosixPath('ecommerce/__init__.py'), PosixPath('ecommerce/shopping')]
# [PosixPath('ecommerce/shopping')]
paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.glob('*.py')] # [PosixPath('ecommerce/__init__.py')]
# [PosixPath('ecommerce/__init__.py')]
py_files = [p for p in path.rglob('*.py')]

print(paths)
print(py_files)
