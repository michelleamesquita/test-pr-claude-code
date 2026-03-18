# Relatório de Segurança Snyk Code

**Projeto:** `test-pr-claude-code`  
**Diretório:** `/Users/mac/Documents/test-pr-claude-code`  
**Data:** 2026-03-18 07:38:50  
**Total de findings:** 2  
**Críticos/Altos:** 1 | **Médios:** 1 | **Baixos:** 0  

**Status de risco:** 🔴 ALTO RISCO — corrija os findings críticos antes do próximo deploy.

---

## 🔴 CRÍTICO/ALTO

### [1] `python/XSS` — `app.py:26`
- **CWE:** N/A
- **Priority Score:** 850/1000
- **Descrição:** Unsanitized input from an HTTP parameter flows into the return value of search, where it is used to render an HTML page returned to the user. This may result in a Cross-Site Scripting attack (XSS).
- **Autofixável (DeepCode AI):** ✅ Sim

## 🟡 MÉDIO

### [1] `python/RunWithDebugTrue` — `app.py:33`
- **CWE:** N/A
- **Priority Score:** 600/1000
- **Descrição:** Running the application in debug mode (debug flag is set to True in run) is a security risk if the application is accessible by untrusted parties.
- **Autofixável (DeepCode AI):** ✅ Sim

---

## 📊 Resumo por categoria

| Categoria | Qtd |
|---|---|
| `python/XSS` | 1 |
| `python/RunWithDebugTrue` | 1 |

---

*Gerado automaticamente pelo hook snyk-stop-report.py*