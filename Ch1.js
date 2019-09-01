// Arrays and Strings

// 1.1: Is Unique
function unique(str) {
    let first;

    for(let i = 0; i < str.length; i++) {
        first = str[0];
        str = str.slice(1);

        if(str.includes(first)) return false
    }

    return true;
}

// 1.2: Check Permutation
function checkPerms(str1, str2) {
    if(str1.length !== str2.length) return false;

    let set2 = new Set();

    for(let i = 0; i < str1.length; i++) {
        set2.add(str2[i]);
    }

    while(str1.length > 0) {
        if(set2.has(str1[0])) {
            str1 = str1.slice(1);
        } else {
            return false;
        }
    }

    return true;
}

// 1.3: URLify 
function urlify(str) {
    const arrStr = str.split("");

    const arrUrl = arrStr.map( (ch) => {
        return ch === " " ? "%20" : ch;
    })

    return arrUrl.join("");
}

// 1.4: Palindrome Permutation
function palindromePerm(str) {
    const hash = {};
    let odds = 0;

    for(let i = 0; i < str.length; i++) {
        if(str[i] !== " ") {
            if(!hash[str[i]]) hash[str[i]] = 0;
            hash[str[i]] += 1;
        }
    }

    const counts = Object.values(hash);

    for(let i = 0; i < counts.length; i++) {
        if(counts[i] % 2 !== 0) odds += 1;
    }

    return odds > 0 ? false : true;
}

// 1.5 One Away

function oneAway(str1, str2) {

    if(Math.abs(str1.length - str2.length) > 1) return false;
    let changes = 0;
    const set1 = new Set();

    for(let i = 0; i < str1.length; i++) {
        set1.add(str1[i]);
    }

    while(str2.length) {
        if(!set1.has(str2[0])) {
            changes += 1;

        }
        str2 = str2.slice(1);
    }

    if(changes > 1) {
        return false;
    } else {
        return true;
    }
}

// 1.6 String Compression

function stringCompression(str) {
    const hash = {};
    let compressed = "";

    for(let i = 0; i < str.length; i++) {
        if(!hash[str[i]]) hash[str[i]] = 0;
        hash[str[i]] += 1;
    }

    Object.keys(hash).forEach(el => {
        compressed += (el + hash[el]);
    })

    return compressed.length < str.length ? compressed : str;
}

// 1.7 Rotate Matrix 
// Given an image represed by an N x N matrix, where each pixel in the image is 4 bytes, write a method
// to rotate the image by 90 degrees. Can you do this in place?

// Input:
// [
//     [1, 2, 3, 4],
//     [5, 6, 7, 8],
//     [9, 10, 11, 12],
//     [13, 14, 15, 16]
// ];
// Output:
// [
//     [13, 9, 5, 1],
//     [14, 10, 6, 2],
//     [15, 11, 7, 3]
//     [16, 12, 8, 4]
// ];

// copy version
function rotateMatrix1(matrix) {
    let rotated = [];

    for(let i = 0; i < matrix.length; i++) {
        rotated.push([]);
    }

    for(let i = 0; i < matrix.length; i++) {
        for(let j = 0; j < matrix[i].length; j++) {
            rotated[j].unshift(matrix[i][j]);
        }
    }
    return rotated;
}

// in place
function rotateMatrix2(matrix) {
    const len = matrix.length;

    // swap rows
    for (let i = 0; i < len / 2; i++) {
        let j = len - i - 1;
        [matrix[i], matrix[j]] = [matrix[j], matrix[i]];
    }

    // swap diagonals
    for (let i = 0; i < len - 1; i++) {
        for (let j = i + 1; j < len; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }

    return matrix;
}



