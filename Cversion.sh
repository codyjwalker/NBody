echo "Building the C versions now:"
make clean
make
echo "Launching C program now:"
./sequential
python3 PythonGraphics.py
