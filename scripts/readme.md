This folder contains some useful scripts and bash commands to process material.

To clone the repository of the user AnaKikDze, use:
```
mkdir AnaKikDze; cd AnaKikDze; git clone https://github.com/AnaKikDze/lingdata; cd ..;
```
The bash file `gitclonerepositories.ssh` based on `repositorylist.txt` can be used to clone all repositories.

To create a list of eaf.files, use:
```
find . -name \*.eaf -type f > eaffilenames.txt
```

To create a list of eaf files with part of speech and gesture annotations, use:
```
find . -name \*-pos.eaf -type f > eaffilenames.txt
find . -name \*-gest.eaf -type f > eaffilenames.txt
```

See `eaf-hw1-filenames.txt` and `eaf-hw1-local-filenames.txt` for (manually corrected) lists of .eaf files resulting from the elan-1 homework assignment.  

To extract annotations from the text@.. tiers without parsing XML trees, I simply extracted annotations that started with Cyrillic words and contained more than one word. The results are saved in `text_tiers_all_annotations.txt`.

```
cat $(grep -v '^#' eaf-hw1-local-filenames.txt) | grep -E -o '>[А-Яа-я]+ .*?<' | cut -d ">" -f2 | cut -d "<" -f1 > text_tiers_all_annotations.txtgrep -E -o '>[А-Яа-я]+ .*?<' | cut -d ">" -f2 | cut -d "<" -f1 > text_tiers_all_annotations.txt
```
(use sed and lookahead/lookbehind regex-es in Linux instead)

