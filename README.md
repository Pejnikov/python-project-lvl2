## Difference Generator
[![Actions Status](https://github.com/Pejnikov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Pejnikov/python-project-lvl2/actions)
![Project tests](https://github.com/Pejnikov/python-project-lvl2/actions/workflows/project-check.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/7fec3cdb17e4fd0c5333/maintainability)](https://codeclimate.com/github/Pejnikov/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7fec3cdb17e4fd0c5333/test_coverage)](https://codeclimate.com/github/Pejnikov/python-project-lvl2/test_coverage)

### 🧨 Key Features
- Supports formats: '.json' and '.yaml'/'.yml';
- Supports two native ouput formats: Plain, Stylish (default);
- Has special JSON ouput.

### 🛠 Installation and Running

#### Package:
```bath
$ python3 -m pip install --user hexlet-code
$ gendiff filepath1 filepath2
```
#### Library:
```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```
### 🪄 Quick Example
```bath
$ cat file1 file2
```
```json
{
    "unmodified": "health",
    "removed": "time",
    "updated": "1000$"
}
{
    "unmodified": "health",
    "added": "knowledge",
    "updated": "10000$"
}
```
```bath
$ gendiff file1 file2
```
```bath
{
  + added: knowledge
  - removed: time
    unmodified: health
  - updated: 1000$
  + updated: 10000$
}
```
```bath
$ gendiff file1 file2 -f plain
```
```bath
Property 'added' was added with value: 'knowledge'
Property 'removed' was removed
Property 'updated' was updated. From '1000$' to '10000$'
```

