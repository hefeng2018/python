/**
 * Created by hefeng on 2018/4/11.
 */

function swiper1() {
    var mySwiper1 = new Swiper('#topSwiper', {
        direction: 'horizontal',
        loop: true,
        speed: 500,
        autoplay: 2000,
        pagination: '.swiper-pagination',
        contorl: true
    })
}

$(function () {
    setTimeout("swiper1()", 1000)
})