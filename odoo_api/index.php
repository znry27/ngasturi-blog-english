<?php 
	require_once('ripcord-master/ripcord.php');

	$url = 'http://localhost:8069';
	$db = 'tutorial_dua';
	$email = 'agus@gmail.com';
	$password = '123';

	$common = ripcord::client("$url/xmlrpc/2/common");
	$uid = $common->authenticate($db, $email, $password, []);
	
	if(!empty($uid)){
		// echo "Successfully sign in with the user id of : " . $uid . '</br>';

		$models = ripcord::client("$url/xmlrpc/2/object");

		// an example of how to call 'search' the public method
		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'search', [[]]);

		// an example of how to call '_search' the private method, it should cause an error
		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', '_search', [[]]);


		// an example of how to call the API with record_ids
		// dengan record_ids berupa array
		// $partner_record_ids = [9,10];
		// $partner_value = [
		// 	'street' => 'Jl. Rajawali 12',
		// 	'city' => 'Surabaya'
		// ];
		// $values = [$partner_record_ids, $partner_value];

		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'write', $values);

		// an example of how to call odoo API with positional argument
		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'search', [[],0,2]);

		// an example of how to call the odoo API with keyword argument
		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'search', [[]], ['order' => 'name desc','limit' => 2]);

		// an example of how to call the create method in res.partner model
		// $values = [
		// 	'name' => 'Ngasturi',
		// 	'street' => 'Jl. Semolowaru 12',
		// 	'city' => 'Surabaya'
		// ];
		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'create', [$values]);

		// an example of how to call the copy method
		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'copy', [[14]], ['default' => ['street' => 'Jl. Ahamad Yani 14']]);

		// an example of how to call the unlink method
		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'unlink', [[14]]);

		// an example of how to call the search method with a domain
		// $domain = [
		// 	['email', 'ilike', 'gmail'],
		// 	['city', '=', 'Surabaya']
		// ];
		// $kwargs = ['order' => 'name desc, street asc', 'limit' => 2];
		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'search', [$domain], $kwargs);

		// $partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'search_count', [$domain]);


		// an example of how to call the search_read method
		$domain = [
			['email', 'ilike', 'gmail'],
			['city', '=', 'Surabaya']
		];
		$kwargs = ['order' => 'name desc, street asc', 'domain' => $domain, 'fields' => ['name', 'city', 'street', 'email']];
		$partners = $models->execute_kw($db, $uid, $password, 'res.partner', 'search_read', [], $kwargs);

		echo "<pre>" . print_r($partners, true) . "</pre>";

	}else{
		echo "Failed to sign in";
	}
?>