def tinh_tien_thuong(x, y):
  """Tính tiền thưởng cho nhân viên.

  Args:
    x: Hiệu suất (1, 0, hoặc -1).
    y: Số năm làm việc (số nguyên).

  Returns:
    Tiền thưởng.
  """
  if x == 1:
    if y < 1:
      return 200
    elif 1 <= y <= 2:
      return 500
    elif 2 < y <= 5:
      return 700
    else:
      return 1000
  elif x == 0:
    if y < 1:
      return 50
    elif 1 <= y <= 2:
      return 100
    elif 2 < y <= 5:
      return 300
    else:
      return 500
  elif x == -1:
    if y < 2: 
      return 0
    else:
      return 100 
  else:
    return "Invalid input"
  

