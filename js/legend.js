function legend(parent, data) {
    parent.className = 'legend_chart';
    var datas = data.hasOwnProperty('datasets') ? data.datasets : data;

    datas.forEach(function(d) {
        var title = document.createElement('span');
        title.className = 'title_chart';
        title.style.borderColor = d.hasOwnProperty('strokeColor') ? d.strokeColor : d.color;
        title.style.borderStyle = 'solid';
        parent.appendChild(title);

        var text = document.createTextNode(d.title);
        title.appendChild(text);
    });
}
