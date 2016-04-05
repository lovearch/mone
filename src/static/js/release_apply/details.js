/**
 * Created by xufengtian on 16-3-18.
 */
$("#worksheet_content").html($("#worksheet_content").attr("content"));

var action_type = '';
var release_apply_id = $('#release_apply_id').val();
var reject_reason = '';

$(".decision").click(function(){
    var this_elt = $(this);
    var tips = $("#tips");
    var reject_advice = $("#reject-advice");
    if (this_elt.hasClass("reject")){
        $("#tips").hide();
        reject_advice.find("label").text("请填写打回原因(必填):");
        reject_advice.show();
        $("#toSave").addClass("disabled");
        action_type = $("#last_action").val();
    } else {
        $("#tips").hide();
        reject_advice.find("label").text("请填写通过意见(选填):");
        reject_advice.show();
        $("#toSave").removeClass("disabled");
        action_type = $("#next_action").val();
    }
});

$("#reject-reason").keyup(function(){
    var this_elt = $(this);
    if ( $.trim(this_elt.val()) != "" ){
        $("#toSave").removeClass("disabled");
    }else{
        $("#toSave").addClass("disabled");
    }
});

$("#toSave").click(function(){
    reject_reason = $("#reject-reason").val();
    $.post("/release_apply/update/releaseapplystate/", {
        action_type: action_type,
        release_apply_id: release_apply_id,
        reject_reason: reject_reason
    }, function(result){
        if (result.status == "200") {
            location.reload();
        }else{
            alert("数据库异常！请联系运维开发人员！")
        }
    }, "json");
});