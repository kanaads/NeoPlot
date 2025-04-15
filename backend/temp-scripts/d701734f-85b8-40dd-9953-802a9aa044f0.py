import React, { useEffect, useRef } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';

export default function CodeEditor({ code, setCode }) {
  const editorRef = useRef(null);

  useEffect(() => {
    if (editorRef.current) {
      editorRef.current.scrollTop = 0;
    }
  }, [code]);

  return (
    <div
      ref={editorRef}
      className="border border-gray-700 rounded-md overflow-auto h-[500px] md:h-[500px] sm:h-[300px]"
    >
      <CodeMirror
        value={code}
        height="100%"
        extensions={[python()]}
        onChange={(value) => setCode(value)}
        theme="dark"
        basicSetup={{ lineNumbers: true, foldGutter: true }}
      />
    </div>
  );
}









































plt.savefig('results/d701734f-85b8-40dd-9953-802a9aa044f0.png')