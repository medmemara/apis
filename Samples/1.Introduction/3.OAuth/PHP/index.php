<?php

require "config.php";

session_start();

// access_token�� �߱޵� ���°� �ƴ϶��, OAuth ���� ���� ����
if(!$_SESSION['access_token'] ) {

	try {
		// Request Token ��û
		$request_token_info = $oauth->getRequestToken($request_token_url, $callback_url);

		// ���� Request Token�� ���� Access Token�� ��ȯ�ϱ� ���� session�� ����.
		$_SESSION["request_token_secret"] = $request_token_info["oauth_token_secret"];

		// ����� ���� URL�� redirect
		header('Location: '.$authorize_url.'?oauth_token='.$request_token_info['oauth_token']);
		exit;
	} catch(OAuthException $E) {
		print_r($E);
		exit;
	}
} else {
// Access Token�� �̹� �߱� �Ǿ� �ִ� ���¸�, ��ū ����
	$oauth->setToken($_SESSION['access_token'],$_SESSION['access_token_secret']);
	$oauth->fetch($api_url."/calendar/category/index.xml");
	$xml = simplexml_load_string($oauth->getLastResponse());

}
?>
<!doctype html>
<html>
<head>
<script>
</script>
</head>

<body>
<ul>
<?php
	foreach($xml->category as $category) {
		echo "<li>";
		echo $category->name;
		echo "</li>";
	}
?>
</ul>
</body>
</html>
