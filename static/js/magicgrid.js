<script src="https://raw.githubusercontent.com/e-oj/Magic-Grid/master/dist/magic-grid.min.js"></script>

let magicGrid = new MagicGrid({
    container: '.container',
    animate: true,
    gutter: 30,
    static: true,
    useMin: true
  });

var masonrys = document.getElementsByTagName("img")

for (let i=0; i<masonrys.length; i++){
    masonrys[i].addEventListener('load', function () {
        magicGrid.positionItems();
    }, false);
}
  
  magicGrid.listen();