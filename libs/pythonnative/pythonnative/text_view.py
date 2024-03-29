from abc import ABC, abstractmethod
from .utils import IS_ANDROID
from .view import ViewBase

# ========================================
# Base class
# ========================================


class TextViewBase(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def set_text(self, text: str) -> None:
        pass

    @abstractmethod
    def get_text(self) -> str:
        pass


if IS_ANDROID:
    # ========================================
    # Android class
    # https://developer.android.com/reference/android/widget/EditText
    # ========================================

    from java import jclass

    class TextView(TextViewBase, ViewBase):
        def __init__(self, context, text: str = "") -> None:
            super().__init__()
            self.native_class = jclass("android.widget.EditText")
            self.native_instance = self.native_class(context)
            self.native_instance.setLines(3)
            self.native_instance.setMaxLines(5)
            self.native_instance.setVerticalScrollBarEnabled(True)
            # self.native_instance.movementMethod = ScrollingMovementMethod()
            self.set_text(text)

        def set_text(self, text: str) -> None:
            self.native_instance.setText(text)

        def get_text(self) -> str:
            return self.native_instance.getText().toString()

else:
    # ========================================
    # iOS class
    # https://developer.apple.com/documentation/uikit/uitextview
    # ========================================

    from rubicon.objc import ObjCClass

    class TextView(TextViewBase, ViewBase):
        def __init__(self, text: str = "") -> None:
            super().__init__()
            self.native_class = ObjCClass("UITextView")
            self.native_instance = self.native_class.alloc().init()
            self.set_text(text)

        def set_text(self, text: str) -> None:
            self.native_instance.setText_(text)

        def get_text(self) -> str:
            return self.native_instance.text()
