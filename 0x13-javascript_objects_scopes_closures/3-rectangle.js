#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';

    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        string += 'X';
      }
      string += '\n';
    }
    const result = string.substring(0, string.length - 1);
    console.log(result);
  }
};
