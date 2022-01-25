// flatpickr 옵션 설정 기능 테스트

let date = new Date();
let thisMonth = new Date(date.getFullYear(), date.getMonth(), 1);
let thisMonthLastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);

const dateSelector = document.querySelector('.dateSelector');
flatpickr.localize(flatpickr.l10ns.ko);
dateSelector.flatpickr({
    local: 'ko',
    inline: true,
    mode: "multiple",
    dateFormat: "Y-m-d",
    defaultDate: ["2022-1-19", "2022-1-25"],
    enable: [{
        from: thisMonth,
        to: thisMonthLastDay
    }, ],
    onChange: function(selectedDates, dateStr, instance) {
        //...
        return false;
        console.log(this);
        console.log(selectedDates, dateStr, instance);

    },

    // enable 위에 2개 잘 사용하면 이전 달 다음 달 선택 불가 기능 가능할듯...?
    // from to 에 변수 집어 넣는 형식으로??
    // 기준일이 오늘 (2022-1-18)인데 해당 표시하고자 하는 월을 받아오면 from: thisMonth, to: thisMonthLastDay 에 입력된 값을 수정해서 사용하면 될듯함
});

// defaultDate에 '년도', '월'값 중 첫 번째 값을 기준으로 달력이 설정되는데
// 이 값을 이용하여 표시하고자 하는 '월'의 달력을 보여주면 될듯?