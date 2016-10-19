# whichscript
Tool to detect the ISO-15924 code of the script used in a text

## Installing

    pip3 install --upgrade .

## Command-line

    python3 detect.py <file.txt

## Python API

```python
    >>> from whichscript.detect import detect_script
    >>> detect_script("北冥有魚，其名曰鯤。鯤之大，不知其幾千里也。")
    'Hant'
    >>> detect_script("all of the people can't be all right all of the time")
    'Latn'
```

