#!/usr/bin/env bash

if [ ! $# -eq 3 ]; then
    echo "Errore sintassi: $0 file.txt cartellaA cartellaB"
    exit 1
fi

if [ ! -f $1 ]; then
    echo "$1 deve essere un file esistente"
    exit 1
fi

if [ ! -d $2 ]; then
    echo "$2 deve essere una directory esistente"
    exit 1
fi

if [ ! -d $3 ]; then
    echo "$3 deve essere una directory esistente"
    exit 1
fi

istruzioni=$( cat $1 )
file=''
estensione=''
count=0
cartA=$2
cartB=$3

for riga in $istruzioni; do
    if [ $count -eq 0 ]; then
        file=$riga
        echo "file = $file"
        let count=$count+1
        continue
    fi
    if [ $count -eq 1 ]; then
        estensione=$riga
        echo "Estensione = $estensione"
        count=0
    fi
    file_senza_estensione=$( echo $file | sed -e 's/\..*//' )
    echo "File senza estensione = $file_senza_estensione"
    new_file="$file_senza_estensione.$estensione"
    echo "New file = $new_file"
    echo "$cartA/$file"
    if [ -f "$cartA/$file" ]; then
        echo "Convert $cartA/$file to $cartA/$new_file"
        mv "$cartA/$file" "$cartA/$new_file"
        echo "Copy $cartA/$new_file to $cartB"
        cp -i "$cartA/$new_file" "$cartB"
    elif [ -f "$cartA/$new_file" ]; then
        echo "Move $cartA/$new_file to $cartB"
        mv -i "$cartA/$new_file" "$cartB"
    fi
done