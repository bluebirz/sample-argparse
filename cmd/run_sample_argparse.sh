run(){
    cmd=$1
    echo "command: $cmd => $(eval $cmd)"
}
run "python3 src/argparse/argparse01_simple.py 1 2"
run "python3 src/argparse/argparse02_list.py 1 2 3 4 5"
run "python3 src/argparse/argparse03_list_choice.py 1 2 3 4 5 -o add"
run "python3 src/argparse/argparse04_web_downloader.py https://toscrape.com sample-scraped-content.html -w"