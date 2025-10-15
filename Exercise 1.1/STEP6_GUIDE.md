# Step 6: Create Copy Environment and Install Requirements

## Purpose
This step demonstrates how `requirements.txt` enables reproducible Python environments. We'll create a second virtual environment (`cf-python-copy`) and install the exact same packages using the requirements file we generated in Step 5.

## Prerequisites
- ✅ `cf-python-base` environment created (Step 2)
- ✅ `ipython` and `bcrypt` installed in `cf-python-base` (Step 3)
- ✅ `requirements.txt` generated from `cf-python-base` (Step 5)

## Commands for Step 6

### 1. Deactivate Current Environment
First, make sure you exit the `cf-python-base` environment:

```powershell
deactivate
```

**Expected output:** The `(cf-python-base)` prefix should disappear from your prompt.

---

### 2. Create New Virtual Environment
Create the second environment called `cf-python-copy`:

```powershell
uv venv cf-python-copy
```

**Expected output:**
```
Using CPython 3.14.0 interpreter at: C:\Users\...\Python\Python314\python.exe
Creating virtual environment at: cf-python-copy
Activate with: cf-python-copy\Scripts\activate
```

---

### 3. Activate cf-python-copy
Activate the newly created environment:

```powershell
.\cf-python-copy\Scripts\Activate.ps1
```

**Expected output:** You should see `(cf-python-copy)` prefix in your prompt.

---

### 4. Install from requirements.txt
Install all packages from the requirements file:

```powershell
uv pip install -r "Exercise 1.1\requirements.txt"
```

**Expected output:**
```
Using Python 3.14.0 environment at: cf-python-copy
Resolved 16 packages in XXms
Installed 16 packages in X.XXs
 + asttokens==3.0.0
 + bcrypt==5.0.0
 + colorama==0.4.6
 + decorator==5.2.1
 + executing==2.2.1
 + ipython==9.6.0
 + ipython-pygments-lexers==1.1.1
 + jedi==0.19.2
 + matplotlib-inline==0.1.7
 + parso==0.8.5
 + prompt-toolkit==3.0.52
 + pure-eval==0.2.3
 + pygments==2.19.2
 + stack-data==0.6.3
 + traitlets==5.14.3
 + wcwidth==0.2.14
```

---

### 5. Verify Installation
Check that all packages were installed:

```powershell
uv pip list
```

**Expected output:** Should show all 16 packages (same as cf-python-base)

---

### 6. Test ipython
Verify ipython works in this environment:

```powershell
ipython --version
```

**Expected output:** `9.6.0`

---

### 7. Compare Both Environments
To prove both environments are identical, compare package lists:

**In cf-python-copy (current):**
```powershell
uv pip list
```

**Then switch to cf-python-base:**
```powershell
deactivate
.\cf-python-base\Scripts\Activate.ps1
uv pip list
```

Both should show the exact same 16 packages with matching versions!

---

## 📸 Screenshot Checklist for Step 6

Take a screenshot that shows:

1. ✅ The `deactivate` command
2. ✅ Creating `cf-python-copy` with `uv venv`
3. ✅ Activating `cf-python-copy` (showing the prefix in prompt)
4. ✅ Installing from requirements.txt with `uv pip install -r`
5. ✅ The list of 16 installed packages
6. ✅ Verifying ipython version

**Suggested screenshot name:** `step6_copy_env.png`

---

## Complete Command Sequence (Copy-Paste Ready)

```powershell
# Deactivate current environment
deactivate

# Create new environment
uv venv cf-python-copy

# Activate it
.\cf-python-copy\Scripts\Activate.ps1

# Install from requirements.txt
uv pip install -r "Exercise 1.1\requirements.txt"

# Verify installation
uv pip list

# Test ipython
ipython --version
```

---

## Verification

### Success Indicators:
- ✅ `(cf-python-copy)` appears in your prompt
- ✅ 16 packages installed successfully
- ✅ `ipython --version` shows `9.6.0`
- ✅ `uv pip list` matches `cf-python-base` packages exactly

### What This Proves:
1. **Requirements.txt works** — All packages installed correctly
2. **Environments are isolated** — cf-python-copy is separate from cf-python-base
3. **Reproducibility** — Same requirements.txt = identical environment
4. **Modern workflow** — Using `uv` for fast, reliable package management

---

## Troubleshooting

### If PowerShell blocks the activate script:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
```

### If uv is not recognized:
```powershell
$env:Path = "C:\Users\$env:USERNAME\.local\bin;$env:Path"
```

### To verify requirements.txt exists:
```powershell
Get-Content "Exercise 1.1\requirements.txt"
```

---

## Why This Step Matters

This demonstrates a **critical Python development workflow**:

1. **Developer A** creates an environment and installs packages
2. **Developer A** exports requirements: `uv pip freeze > requirements.txt`
3. **Developer B** receives the code and requirements.txt
4. **Developer B** creates environment: `uv venv project-env`
5. **Developer B** installs dependencies: `uv pip install -r requirements.txt`
6. **Both developers have identical setups!**

This is how teams ensure everyone works with the same package versions, preventing "works on my machine" issues.

---

## Next Steps

After completing Step 6:
1. ✅ Take screenshot showing the complete process
2. ✅ Save as `screenshots/step6_copy_env.png`
3. ✅ Deactivate the environment: `deactivate`
4. ✅ Update your learning journal with what you learned
5. ✅ Ready to submit to GitHub!

---

**Current Status:** cf-python-copy environment already exists ✅  
**Packages installed:** Ready to verify  
**Ready for screenshot:** Yes!
