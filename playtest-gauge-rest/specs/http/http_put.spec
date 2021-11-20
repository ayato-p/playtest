# HTTP PUT リクエストを送信するステップのテスト

tags: http-request-test

## PUTリクエストを送信できる
* URL"/"にPUTリクエストを送る
* URL"/"にPUTリクエストが送信された

## PUTリクエストに対するレスポンスをアサートできる
* URL"/"にPUTリクエストを送る
* HTTPレスポンスステータスコードが"200"である
* レスポンスヘッダーに"x-example-header"が存在し、その値が"example1"である
* レスポンスのJSONの"$.message"が文字列の"OK"である

## リクエストボディを指定してPUTリクエストを送信できる
* URL"/"にリクエストボディ"{\"test\": \"test\"}"で、PUTリクエストを送る
* URL"/"にリクエストボディ"{\"test\": \"test\"}"で、PUTリクエストが送信された

## リクエストヘッダーを指定してPUTリクエストを送信できる
* URL"/"にリクエストヘッダー"content-type: application/json"で、PUTリクエストを送る
* URL"/"にリクエストヘッダー"content-type: application/json"で、PUTリクエストが送信された

## リクエストボディとリクエストヘッダーを指定してPUTリクエストを送信できる
* URL"/"にリクエストボディ"{\"test\": \"test\"}"、リクエストヘッダー"content-type: application/json"で、PUTリクエストを送る
* URL"/"にリクエストボディ"{\"test\": \"test\"}"、リクエストヘッダー"content-type: application/json"で、PUTリクエストが送信された