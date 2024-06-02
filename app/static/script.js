$(document).ready(function() {
    $('#calendar').fullCalendar({
        editable: true,
        selectable: true,
        selectHelper: true,
        select: function(start, end, jsEvent, view) {
            $("#tooltip").css({
                position: "absolute",
                left: jsEvent.pageX,
                top: jsEvent.pageY
            }).show();

            $("#createEvent").off().on("click", function() {
                window.location.href = "/event";
            });

            $("#createMeeting").off().on("click", function() {
                window.location.href = "/meeting";
            });

            $("#createTask").off().on("click", function() {
                window.location.href = "/task";
            });

            $('body').on('click', function() {
                $("#tooltip").hide();
            });

            return false;
        }
    });
});
