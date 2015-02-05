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

        $("#createCourseForm").submit(function(){
            var data = [];
            $(".specialties").each(function(){
                var temp = {};
                temp.id = $(this).parent().data("id");
                temp.specialty = $(this).val();
                temp.semester = $(this).parent().find(".semesters").val();
                data.push(temp);
            });
            data = JSON.stringify(data);
            $("#id_specialtyData").val(data);
        });

Dropzone.options.myAwesomeDropzone = false;
Dropzone.autoDiscover = false;


var myDropzone = new Dropzone("#my-awesome-dropzone", {
    paramName: "file", // The name that will be used to transfer the file
    maxFilesize: 2, // MB
    createImageThumbnails: true,
    thumbnailWidth: 100,
    thumbnailHeight: 100,
    autoProcessQueue: false,
    addRemoveLinks: "remove",
    dictRemoveFile: "Изтрий",
    init: function() {
        var myDropzone = this;
        this.element.querySelector("#my-awesome-dropzone input[type=submit]").addEventListener("click", function(e) {
            e.preventDefault();
            e.stopPropagation();
            myDropzone.processQueue();
        });
    },
    success: function(){
        $(location).attr('href', "/lector/profile/#success");
        location.reload();
    },
    error: function(){
        $(location).attr('href', "/lector/profile/#error");
        location.reload();
    }
});

    $(".openCourse").click(function(){
        $("section>div").hide();
        $("#uploaded").show().find("tbody").html("");
        var course_id = $(this).attr("href").split("=")[1];
        $.ajax({
            type: "GET",
            url: "/course/get_course_files/" + course_id,
        }).done(handle_file_response);
    });

    $("table").on("click", ".delete", function(){
        var $this = $(this);
        $.ajax({
            type: "GET",
            url: $(this).data("href"),
        }).done(function() {
            $this.closest("tr").remove();
        });
    })

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
            el += "<a href=/media/" + e.path + ">Свали</a>";
            el += "</td><td>";
            el += "<a class='delete' href=" + location.href + " data-href='/lector/delete?path=" + e.path + "'>Изтрий</a>";
            el += "</td></tr>";
            $("tbody").append(el);
        });
    }

    $(".save").click(function(){
        var $task = $(".newTask")
        var packet = {
            "course": $task.find("select").val(),
            "description": $task.find("textarea").val(),
            "date": $task.find("input[type=date]").val(),
            "time": $task.find("input[type=time]").val()
        }
        $.ajax({
            type: "GET",
            url: "/task/create/",
            data: packet
        }).done(function(){
            location.reload();
        });
    })