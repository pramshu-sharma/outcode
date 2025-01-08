The leetcode solutions are in the leetcode folder.

To use the bit.ly clone app please follow the steps:

1. Clone the repo.
2. Create a virtual environment and install requirements.
3. Apply Django migrations.
4. Run the development server.

URL routes:
/ (root) - For creating hash IDs to shorten URLs.
/<str:hash_id> - For redirecting to the original URL via the hashed URL.

Screenshots:

When a URL is created:
![image](https://github.com/user-attachments/assets/5c97dc16-a731-4f6c-b527-99d25b6be68c)

Invalid URL:
![image](https://github.com/user-attachments/assets/ea7ef7f3-2525-46a7-b145-09096bc0f759)

404:
![image](https://github.com/user-attachments/assets/26238699-e4ae-40f6-905d-7860c364527b)

