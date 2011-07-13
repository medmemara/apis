<?php
require "config.php";

session_start();
if($_GET['oauth_verifier'] ) {
	try {
		// Request Token�� verifier�� Access Token ���
		$oauth->setToken($_GET['oauth_token'],$_SESSION["request_token_secret"]);
		$access_token_info = $oauth->getAccessToken($access_token_url, null, $_GET['oauth_verifier']);

		// Access Token���� ��ȯ �Ǿ����Ƿ� Request Token ����.
		unset($_SESSION["request_token_secret"]);
		
		// Access Token�� ���ǿ� ����
		$_SESSION['access_token'] = $access_token_info['oauth_token'];
		$_SESSION['access_token_secret'] = $access_token_info['oauth_token_secret'];
	} catch(OAuthException $E) {
		print_r($E);
		exit;
	}
}
// protected resource�� �ִ� ��������
header("Location: ./index.php");
?>
