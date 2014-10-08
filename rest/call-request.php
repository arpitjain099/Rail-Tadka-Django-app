<?php
	// Include the Twilio PHP library
	require 'twilio-php-master/Services/Twilio.php';

	// Twilio REST API version
	$version = "2010-04-01";

	// Set our Account SID and AuthToken
	$sid = 'AC77709cad71509b163f6f3ec522c8c7da';
	$token = 'c858b7751cc0d1260efbe9153ef5f8b4';
	
	// A phone number you have previously validated with Twilio
	$phonenumber = '7045869183';
	
	// Instantiate a new Twilio Rest Client
	$client = new Services_Twilio($sid, $token, $version);

	try {
		// Initiate a new outbound call
		$call = $client->account->calls->create(
			$phonenumber, // The number of the phone initiating the call
			'918960482697', // The number of the phone receiving call
			'http://demo.twilio.com/welcome/voice/' // The URL Twilio will request when the call is answered
		);
		echo 'Started call: ' . $call->sid;
	} catch (Exception $e) {
		echo 'Error: ' . $e->getMessage();
	}
