def tinh_tien_thuong(hieu_suat, so_nam_lam_viec):
  """Tính tiền thưởng cho nhân viên.

  Args:
    hieu_suat: Hiệu suất (1, 0, hoặc -1).
    so_nam_lam_viec: Số năm làm việc (số nguyên).

  Returns:
    Tiền thưởng.
  """
  if hieu_suat == 1:
    if so_nam_lam_viec < 1:
      return 200
    elif 1 <= so_nam_lam_viec <= 2:
      return 500
    elif 2 < so_nam_lam_viec <= 5:
      return 700
    else:
      return 1000
  elif hieu_suat == 0:
    if so_nam_lam_viec < 1:
      return 50
    elif 1 <= so_nam_lam_viec <= 2:
      return 200
    elif 2 < so_nam_lam_viec <= 5:
      return 300
    else:
      return 500
  elif hieu_suat == -1:
    return 0 # Lỗi: thiếu kiểm tra số năm làm việc
  else:
    return "Đầu vào không hợp lệ"