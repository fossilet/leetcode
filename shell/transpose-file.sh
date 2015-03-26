#! /bin/bash

#https://leetcode.com/problems/transpose-file/
#
#Given a text file file.txt, transpose its content.
#
#You may assume that each row has the same number of columns and each field is separated by the ' ' character.
#
#For example, if file.txt has the following content:
#
#name age
#alice 21
#ryan 30
#Output the following:
#
#name alice ryan
#age 21 30

awk '{
    for (i = 1; i <= NF; i++) {
        A[i, FNR]=$i }
    }
END {
    for (j = 1; j <= NF; j ++) {
        for (i= 1; i<= NR; i++) {
            if (i == NR) {
                print A[j, i]
            } else {
                printf "%s ", A[j,i]
            }
        }
    }
}' file.txt
