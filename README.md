### Bài tập về nhà môn Kiểm thử và Đảm bảo chất lượng phần mềm
Sinh viên: Lê Thế Phương Minh

MSSV: 22028089
#### Mô tả bài toán
Một công ty muốn tính toán tiền thưởng cho nhân viên dựa trên hai yếu tố: **Hiệu suất** và **Thâm niên**

Quy tắc tính thưởng:
- Nếu hiệu suất "Tốt":
    - Dưới 1 năm: 200
    - Từ 1 đến 2 năm: 500
    - Từ 2 đến 5 năm: 700
    - Trên 5 năm: 1000
- Nếu hiệu suất "Trung bình":
    - Dưới 1 năm: 50
    - Từ 1 đến 2 năm: 100
    - Từ 2 đến 5 năm: 300
    - Trên 5 năm: 500
- Nếu hiệu suất "Kém": 0 bất kể số năm làm việc.

Input:
- Hiệu suất: int x với Tốt: x=1; Trung bình: x=0; Kém: x=-1
- Thâm niên: float y; y>=0
Output
- int z 
#### Báo cáo kiểm thử
1. Kiểm thử giá trị biên

| ID  | Input x | Input y | Expected Output | Actual Output | Result |
| --- | ------- | ------- | --------------- | ------------- | ------ |
| 1   | -1      | 0       | 0               | 0             | Passed |
| 2   | -1      | 1       | 0               | 0             | Passed |
| 3   | -1      | 15      | 0               | 100           | Failed |
| 4   | -1      | 99      | 0               | 100           | Failed |
| 5   | -1      | 100     | 0               | 100           | Failed |
| 6   | 0       | 0       | 50              | 50            | Passed |
| 7   | 0       | 1       | 100             | 100           | Passed |
| 8   | 0       | 15      | 500             | 500           | Passed |
| 9   | 0       | 99      | 500             | 500           | Passed |
| 10  | 0       | 100     | 500             | 500           | Passed |
| 11  | 1       | 0       | 200             | 200           | Passed |
| 12  | 1       | 1       | 500             | 500           | Passed |
| 13  | 1       | 15      | 1000            | 1000          | Passed |
| 14  | 1       | 99      | 1000            | 1000          | Passed |
| 15  | 1       | 100     | 1000            | 1000          | Passed |
1.  Kiểm thử bảng quyết định
Xác định các điều kiện:
- C1: x < -1
- C2: x=-1
- C3: x=0
- C4: x=1
- C5: x > 1
- C6: y < 0
- C7: 0 <= y < 1
- C8: 1 <= y < 2
- C9: 2<= y < 5
- C10: 5 <= y < 150
- C11: y >= 150
Xác định hành động
- E1: Input không hợp lệ
- E2: Tính thưởng 200
- E3: Tính thưởng 500
- E4: Tính thưởng 700
- E5: Tính thưởng 1000
- E6: Tính thưởng 50
- E7: Tính thưởng 100
- E8: Tính thưởng 300
- E9: Tính thưởng 500
- E10: Tính thưởng 0

Bảng quyết định

| TC        |     | TC1 | TC2 | TC3 | TC4 | TC5 | TC6 | TC7 | TC8 | TC9 | TC10 | TC11 | TC12 | TC13 | TC14 | TC15 | TC16 |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Điều kiện | C1  | T   | F   | F   | F   | F   | F   | F   | F   | F   | F    | F    | F    | F    | F    | F    | F    |
|           | C2  | -   | T   | T   | F   | F   | F   | F   | F   | F   | F    | F    | F    | F    | F    | F    | F    |
|           | C3  | -   | -   | -   | T   | T   | T   | T   | T   | T   | F    | F    | F    | F    | F    | F    | F    |
|           | C4  | -   | -   | -   | -   | -   | -   | -   | -   | -   | T    | T    | T    | T    | T    | T    | F    |
|           | C5  | -   | -   | -   | -   | -   | -   | -   | -   | -   | -    | -    | -    | -    | -    | -    | T    |
|           | C6  | -   | T   | F   | T   | F   | F   | F   | F   | F   | T    | F    | F    | F    | F    | F    | -    |
|           | C7  | -   | -   | -   | -   | T   | F   | F   | F   | F   | -    | T    | F    | F    | F    | F    | -    |
|           | C8  | -   | -   | -   | -   | -   | T   | F   | F   | F   | -    | -    | T    | F    | F    | F    | -    |
|           | C9  | -   | -   | -   | -   | -   | -   | T   | F   | F   | -    | -    | -    | T    | F    | F    | -    |
|           | C10 | -   | -   | -   | -   | -   | -   | -   | T   | F   | -    | -    | -    | -    | T    | F    | -    |
|           | C11 | -   | -   | -   | -   | -   | -   | -   | -   | T   | -    | -    | -    | -    | -    | T    | -    |
| Hành động | E1  | T   | T   | F   | T   | F   | F   | F   | F   | T   | T    | F    | F    | F    | F    | T    | T    |
|           | E2  | -   | -   | F   | -   | F   | F   | F   | F   | -   | -    | T    | F    | F    | F    | -    | -    |
|           | E3  | -   | -   | F   | -   | F   | F   | F   | F   | -   | -    | F    | T    | F    | F    | -    | -    |
|           | E4  | -   | -   | F   | -   | F   | F   | F   | F   | -   | -    | F    | F    | T    | F    | -    | -    |
|           | E5  | -   | -   | F   | -   | F   | F   | F   | F   | -   | -    | F    | F    | F    | T    | -    | -    |
|           | E6  | -   | -   | F   | -   | T   | F   | F   | F   | -   | -    | F    | F    | F    | F    | -    | -    |
|           | E7  | -   | -   | F   | -   | F   | T   | F   | F   | -   | -    | F    | F    | F    | F    | -    | -    |
|           | E8  | -   | -   | F   | -   | F   | F   | T   | F   | -   | -    | F    | F    | F    | F    | -    | -    |
|           | E9  | -   | -   | F   | -   | F   | F   | F   | T   | -   | -    | F    | F    | F    | F    | -    | -    |
|           | E10 | -   | -   | T   | -   | F   | F   | F   | F   | -   | -    | F    | F    | F    | F    | -    | -    |

Báo cáo kiểm thử

| ID  | Input x | Input y | Expected Output | Actual Output | Result |
| --- | ------- | ------- | --------------- | ------------- | ------ |
| 1   | -2      | 15      | Invalid input   | Invalid input | Passed |
| 2   | -1      | -1      | Invalid input   | 0             | Failed |
| 3   | -1      | 10      | 0               | 100           | Failed |
| 4   | 0       | -1      | Invalid input   | 50            | Failed |
| 5   | 0       | 0.5     | 50              | 50            | Passed |
| 6   | 0       | 1.5     | 100             | 100           | Passed |
| 7   | 0       | 2.5     | 300             | 300           | Passed |
| 8   | 0       | 6       | 500             | 500           | Passed |
| 9   | 0       | 152     | Invalid input   | 500           | Failed |
| 10  | 1       | -1      | Invalid input   | 200           | Failed |
| 11  | 1       | 0.5     | 200             | 200           | Passed |
| 12  | 1       | 1.5     | 500             | 500           | Passed |
| 13  | 1       | 2.5     | 700             | 700           | Passed |
| 14  | 1       | 6       | 1000            | 1000          | Passed |
| 15  | 1       | 152     | Invalid input   | 1000          | Failed |
| 16  | 2       | 15      | Invalid input   | Invalid input | Passed |
