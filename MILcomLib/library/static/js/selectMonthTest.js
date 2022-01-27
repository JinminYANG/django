$(function() {

    const today = new Date();
    const setDay = 1;   // '월' 값을 기준으로 처리하기 위한 '1' 사용
    const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), setDay);
    const lastMonth = new Date(firstDayOfMonth.setDate(firstDayOfMonth.getDate() - setDay));

    var statisticsMonth = $("#statisticsMonth").kendoDatePicker({
        culture: "ko-KR",
        start: "year",
        depth: "year",
        format: "yyyy년 MM월",
        max: lastMonth,
    }).data("kendoDatePicker");

    // input 클릭 시 datepicker가 open 되는 기능을 위한 테스트 코드
    var statisticsMonthpicker = $("#statisticsMonth").data("kendoDatePicker");
    $("#statisticsMonth").click(function () {
        statisticsMonthpicker.open();
    });

    // 텍스트 입력을 막기 위한 코드
    $("#statisticsMonth").on("keydown", function (e) {
        e.preventDefault();
    });

    // 대시보드 페이지 달력(월) 선택기능 일시정지
    statisticsMonthpicker.enable(false);

});