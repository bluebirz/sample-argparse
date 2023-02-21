run(){
    cmd=$1
    echo "command: $cmd => $(eval $cmd)"
}

run "python3 src/argv/argv01_simple.py 1 2"
run "python3 src/argv/argv02_list.py 1 2 3 4 5"