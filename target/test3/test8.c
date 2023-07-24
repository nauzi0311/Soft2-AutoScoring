#include <stdio.h>

int main(int argc, char const *argv[])
{
    FILE* fp;
    if((fp = fopen(argv[1],"r")) == NULL){
        printf("Can't open file: %s",argv[1]);
        return -1;
    }
    FILE* fpo;
    if((fpo = fopen(argv[2],"w")) == NULL){
        printf("Can't open file: %s",argv[2]);
        return -1;
    }
    char c;
    while((c = fgetc(fp)) != EOF){
        fprintf(fpo,"%c",c);
    }
    fclose(fp);
    return 0;
}