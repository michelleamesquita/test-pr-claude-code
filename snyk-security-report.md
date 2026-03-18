# Relatório de Segurança Snyk Code

**Projeto:** `test-pr-claude-code`  
**Diretório:** `/Users/mac/Documents/test-pr-claude-code`  
**Data:** 2026-03-18 07:53:26  
**Total de findings:** 6  
**Críticos/Altos:** 3 | **Médios:** 3 | **Baixos:** 0  

**Status de risco:** 🔴 ALTO RISCO — corrija os findings críticos antes do próximo deploy.

---

## 🔴 CRÍTICO/ALTO

### [1] `python/XSS` — `app.py:52`
- **CWE:** N/A
- **Priority Score:** 850/1000
- **Descrição:** Unsanitized input from an HTTP parameter flows into the return value of search, where it is used to render an HTML page returned to the user. This may result in a Cross-Site Scripting attack (XSS).
- **Autofixável (DeepCode AI):** ✅ Sim

### [2] `python/Sqli` — `app.py:68`
- **CWE:** N/A
- **Priority Score:** 834/1000
- **Descrição:** Unsanitized input from a web form flows into execute, where it is used in an SQL query. This may result in an SQL Injection vulnerability.
- **Autofixável (DeepCode AI):** ✅ Sim

### [3] `python/Sqli` — `app.py:94`
- **CWE:** N/A
- **Priority Score:** 834/1000
- **Descrição:** Unsanitized input from an HTTP parameter flows into execute, where it is used in an SQL query. This may result in an SQL Injection vulnerability.
- **Autofixável (DeepCode AI):** ✅ Sim

## 🟡 MÉDIO

### [1] `python/XSS` — `app.py:73`
- **CWE:** N/A
- **Priority Score:** 600/1000
- **Descrição:** Unsanitized input from a database flows into the return value of login, where it is used to render an HTML page returned to the user. This may result in a Cross-Site Scripting attack (XSS).
- **Autofixável (DeepCode AI):** ✅ Sim

### [2] `python/XSS` — `app.py:103`
- **CWE:** N/A
- **Priority Score:** 600/1000
- **Descrição:** Unsanitized input from a database flows into the return value of get_user, where it is used to render an HTML page returned to the user. This may result in a Cross-Site Scripting attack (XSS).
- **Autofixável (DeepCode AI):** ✅ Sim

### [3] `python/RunWithDebugTrue` — `app.py:106`
- **CWE:** N/A
- **Priority Score:** 567/1000
- **Descrição:** Running the application in debug mode (debug flag is set to True in run) is a security risk if the application is accessible by untrusted parties.
- **Autofixável (DeepCode AI):** ✅ Sim

---

## 📊 Resumo por categoria

| Categoria | Qtd |
|---|---|
| `python/XSS` | 3 |
| `python/Sqli` | 2 |
| `python/RunWithDebugTrue` | 1 |

---

*Gerado automaticamente pelo hook snyk-stop-report.py*