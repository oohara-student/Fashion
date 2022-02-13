var strUrl = "https://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid=e177bee6fe91b47685ca733fa0a9a81f";
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    // 非同期通信（Ajax）
    // readyState 4: リクエスト終了, status 200:通信成功
    if (this.readyState == 4 && this.status == 200) {
        var data = this.response;
        // 天気
        document.getElementById('weather').innerHTML = data.weather[0].main;
        var img = document.getElementById('icon');
        img.src = "https://openweathermap.org/img/wn/" + data.weather[0].icon + "@2x.png";
        img.alt = data.weather[0].main;
        // 気温
        document.getElementById('temp').innerHTML = Math.floor((data.main.temp - 273.15) * 100) / 100;
    }
}
xmlhttp.open("GET", strUrl, true);
xmlhttp.responseType = 'json'; // JSONを取得するために必要
xmlhttp.send();