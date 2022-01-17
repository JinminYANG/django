$(function() {
    // 데이터가 지난 달 기준이기 때문에 이번 달 disable 처리를 위한 코드
    const today = new Date();
    const setDay = 1;   // '월' 값을 기준으로 처리하기 위한 '1' 사용
    const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), setDay);
    const lastMonth = new Date(firstDayOfMonth.setDate(firstDayOfMonth.getDate() - setDay));
    // 1월 이지만 0월로 계산되기 때문에 에러가 있음 => 0월을 작년 12월로 대체 하는 과정 (기준이 저번 달이기 때문)
    // 데이터가 없는 달 테스트를 위한 코드
    var disabledMonths = ["2021/2/1", "2021/4/1"];
    // 데이터를 위와 같은 형식으로 받아오면 처리할 수 있게 정의
    // '일'의 값에 1이 들어가야 disabled 처리가 가능하다. ('해당 월'/'1')

    $("#statisticsMonth").kendoDatePicker({
        start: "year"
    });

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