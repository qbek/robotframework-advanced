import io.restassured.RestAssured;

public class Todoist {


    public void getAllProjects() {

        RestAssured
                .given()
                    .header("Authorization", "Bearer <token>")
                    .log().all()
                .when().get("https://api.todoist.com/rest/v1/projects")
                .then().log().all();

    }

}
