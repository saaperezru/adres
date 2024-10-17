print_data() {
    echo "file_name,cufe,pages,size_bytes"
    for i in $(ls $1); do 
        echo -e "$i,$(pdftotext -raw $1/$i - | grep -Pzo '(\b([0-9a-fA-F]\n*){95,100}\b)' | tr -d '\n'),$(pdfinfo $1/$i | grep Pages | sed 's/[^0-9]*//'),$(pdfinfo $1/$i | grep 'File size' | grep -Po '(?<=\D )(\d+)')"; 
    done ;
}

if [ "$#" -lt 2 ]; then
   echo "Usage: ${FUNCNAME[0]} [PDF_FOLDER] [DB_PATH]"
 else
    sqlite3 $2 <<EOF
CREATE TABLE files
(
    file_name TEXT PRIMARY KEY,
    cufe TEXT,
    pages INTEGER,
    size_bytes INTEGER 
);
EOF
    print_data $1 2> /dev/null | sqlite3 -csv $2 ".import '|cat -' files" 
fi
