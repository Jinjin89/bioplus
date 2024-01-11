def df2xlsx(dicts_of_dfs,xlsx_file,**kwargs):
  import pandas as pd
  import os
  assert isinstance(dicts_of_dfs, pd.DataFrame) or isinstance(dicts_of_dfs, dict), "Input must be a DataFrame or a dictionary."
  # 1) check the xlsx file exisits
  if os.path.isfile(xlsx_file):
     print(f"The {xlsx_file} found, overwrite it!")
  with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
    if isinstance(dicts_of_dfs, pd.DataFrame):
       dicts_of_dfs.to_excel(writer, sheet_name=sheet_name,**kwargs)
    else:
      # Iterate over the dictionary and write each DataFrame as a separate sheet
      for sheet_name, df in dicts_of_dfs.items():
          df.to_excel(writer, sheet_name=sheet_name, index=False,**kwargs)
