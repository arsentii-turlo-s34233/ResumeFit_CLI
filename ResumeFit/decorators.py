import functools
from ResumeFit.exceptions import DocumentsNotLoadedError

def require_loaded_docs(func):
    @functools.wraps(func)
    def wrapper(resume_document, job_document):
        if resume_document is None or job_document is None:
            raise DocumentsNotLoadedError("Please load both resume and job description first.")
        return func(resume_document, job_document)

    return wrapper
