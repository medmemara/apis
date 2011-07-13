import java.util.Scanner;

import org.scribe.builder.ServiceBuilder;
import org.scribe.model.OAuthRequest;
import org.scribe.model.Response;
import org.scribe.model.Token;
import org.scribe.model.Verb;
import org.scribe.model.Verifier;
import org.scribe.oauth.OAuthService;

public class OuathProvider {
	public static void main(String[] args) {
		//OAuth �غ�
		OAuthService service = new ServiceBuilder()
		.provider(DaumDnaApi.class)
		.apiKey("eb3eff10-b95d-455c-8572-e7858a2b34d0")
		.apiSecret("suz6.HUjzlaG-S9ezBzFQ11FtKhQvv8cdT-9C_hWBFthpUmMTsOuUA00")
		.callback("oob")
		.build();

		Scanner in = new Scanner(System.in);
		
		// 1. request token �ޱ�
	    Token requestToken = service.getRequestToken();

	    // 2. ����� ���� �ϱ�
	    System.out.println("���������� �����Ͽ� ���� URL�� �����ϼ���.");
	    System.out.println(service.getAuthorizationUrl(requestToken) + "?" + requestToken.getRawResponse());
	    System.out.print("������������ ���� �� ��ȯ �� ���� �Է��ϼ���:");
	    Verifier verifier = new Verifier(in.nextLine());
	    System.out.println();

	    // 3. ���� �� ���� Verifier���� �̿��Ͽ� ������ ��ū ���
	    Token accessToken = service.getAccessToken(requestToken, verifier);
	    
	    // '���� ���Կ��� Ȯ���ϱ�' API�� ���� ���� Ȯ���ϱ�
	    OAuthRequest request = new OAuthRequest(Verb.GET, "https://apis.daum.net/yozm/v1_0/user/joined.xml");
	    service.signRequest(accessToken, request);
	    Response response = request.send();
	    System.out.println(response.getBody());
	    System.out.println();
	}

}
