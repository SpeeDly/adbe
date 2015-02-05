$("section>div").hide();

switch(location.hash){
    case "#success":
        $("#success").show();
        break;
    case "#error":
        $("#error").show();
        break;
    case "#createCourse":
        $("#createCourse").show();
        break;
    case "#upload":
        $("#uploadLectures").show();
        break;
    case "#addTask":
        $("#addTask").show();
        break;
    default:
        if(location.hash.split("course=").length > 1){
            $("#uploaded").show().find("tbody").html("");
            $.ajax({
                type: "GET",
                url: "/course/get_course_files/" + location.hash.split("course=")[1],
            }).done(handle_file_response);
        }
        else{
            $("section div#default").show();            
        }
        break;
}


    $('*[data-open="createCourse"]').click(function(){
        $("section>div").hide();
        $("#createCourse").show();
    })

    $('.upload_wrapper a').click(function(){
        $("section>div").hide();
        $("#uploadLectures").show();
    })
    
    $(".new_field").click(function(){
        var $last = $(".course_options").last();
        $last.after($last.data("id", parseInt($last.data("id")) + 1).clone());
    });

    $(".remove_field").click(function(){
        var $last = $(".course_options").last();
        if($(".course_options").length > 1){
            $last.remove();            
        }
    });

    $(".addTask").click(function(){
        $("section>div").hide();
        $("#addTask").show();
    })

$(".openCourse").click(function(){
    $("section>div").hide();
    $("#uploaded").show().find("tbody").html("");
    var course_id = $(this).attr("href").split("=")[1];
    $.ajax({
        type: "GET",
        url: "/course/get_course_files/" + course_id,
    }).done(handle_file_response);
});

function handle_file_response(data){
    if(data.length === 0){
        $("tbody").append("<tr><td colspan='5'>Тук нямате още качени материали ;(</td></tr>");                
    }
    data.forEach(function(e){
        var el = "<tr><td>";
        el += e.name;
        el += "</td><td>";
        el += e.created;
        el += "</td><td>";
        el += e.size;
        el += "</td><td>";
        el += "<a href=/download?prev=" + location.href + "&file=/media/" + e.path + ">Свали</a>";
        el += "</td><td>";
        el += e.uploaded_by;
        el += "</td></tr>";
        $("tbody").append(el);
    });
}