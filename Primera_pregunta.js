var sum = 1000
for (var a = 1; a <= sum ; a++) {
    for (b = a + 1; b <= sum; b++) {
        var c = sum - a - b;
        if (a * a + b * b == c * c) {
            console.log('a=' + a + 'b=' + b + 'c=' + c);
        }
    }
}
