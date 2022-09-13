# setup for test and dev.

```
python3.8 -m venv env
. env/bin/activate

pip install --editable . 
```

Executando teste no assembly:

```
cd tests/assembly
pytest
```

Executando teste no vm:

```
cd tests/vm-examples
pytest
```
